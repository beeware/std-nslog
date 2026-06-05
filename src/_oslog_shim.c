/*
 * std-nslog: native shim that emits messages via Apple's unified logging
 * system (os_log).
 *
 * os_log() is a preprocessor macro defined in <os/log.h>; it cannot be called
 * from ctypes because it expands to a call to _os_log_impl() which expects a
 * compile-time format-string blob in the binary's __TEXT,__oslog section.
 * This module exists so that the macro is expanded by the C compiler when the
 * wheel is built, and the resulting object code is invoked from Python.
 *
 * The module exposes two functions to Python:
 *
 *   emit(level: int, message: bytes) -> None
 *       Emit `message` (a UTF-8 byte string) at the given os_log_type_t
 *       level using the active log handle.
 *
 *   OS_LOG_TYPE_DEFAULT / _INFO / _DEBUG / _ERROR / _FAULT
 *       Module-level int constants matching <os/log.h>.
 */

#define PY_SSIZE_T_CLEAN

#include <Python.h>

#include <os/log.h>
#include <stdint.h>
#include <string.h>


static PyObject *
shim_emit(PyObject *self, PyObject *args)
{
    unsigned char level = 0;
    const char *msg = NULL;
    Py_ssize_t msg_len = 0;

    if (!PyArg_ParseTuple(args, "By#", &level, &msg, &msg_len)) {
        return NULL;
    }

    /*
     * %{public}s prevents the unified logging subsystem from redacting
     * the message body as <private>, matching NSLog's behavior. The
     * compiler builds the matching __oslog format blob at this site.
     *
     * The message must be a NUL-terminated C string; PyArg_ParseTuple
     * with "y#" guarantees that, but does not reject embedded NULs --
     * those will simply truncate the visible portion. The Python side
     * is responsible for stripping them.
     */
    switch (level) {
        case OS_LOG_TYPE_INFO:
            os_log_info(OS_LOG_DEFAULT, "%{public}s", msg);
            break;
        case OS_LOG_TYPE_DEBUG:
            os_log_debug(OS_LOG_DEFAULT, "%{public}s", msg);
            break;
        case OS_LOG_TYPE_ERROR:
            os_log_error(OS_LOG_DEFAULT, "%{public}s", msg);
            break;
        case OS_LOG_TYPE_FAULT:
            os_log_fault(OS_LOG_DEFAULT, "%{public}s", msg);
            break;
        case OS_LOG_TYPE_DEFAULT:
        default:
            os_log(OS_LOG_DEFAULT, "%{public}s", msg);
            break;
    }

    (void)msg_len;
    Py_RETURN_NONE;
}

static PyMethodDef shim_methods[] = {
    {"emit", shim_emit, METH_VARARGS,
     "emit(level, message): write `message` to the unified log at `level`."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef shim_moduledef = {
    PyModuleDef_HEAD_INIT,
    "_oslog_shim",
    "Native bridge from std-nslog to Apple's unified logging (os_log).",
    -1,
    shim_methods,
    NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC
PyInit__oslog_shim(void)
{
    PyObject *m = PyModule_Create(&shim_moduledef);
    if (m == NULL) {
        return NULL;
    }

#define ADD_INT_CONSTANT(name) \
    if (PyModule_AddIntConstant(m, #name, (long)name) < 0) { \
        Py_DECREF(m); \
        return NULL; \
    }

    ADD_INT_CONSTANT(OS_LOG_TYPE_DEFAULT)
    ADD_INT_CONSTANT(OS_LOG_TYPE_INFO)
    ADD_INT_CONSTANT(OS_LOG_TYPE_DEBUG)
    ADD_INT_CONSTANT(OS_LOG_TYPE_ERROR)
    ADD_INT_CONSTANT(OS_LOG_TYPE_FAULT)

    return m;
}
