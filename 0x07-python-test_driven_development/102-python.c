#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    Py_ssize_t size;
    Py_UNICODE *unicode_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p)) {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    size = PyUnicode_GET_SIZE(p);
    unicode_str = PyUnicode_AsUnicode(p);

    printf("  type: compact unicode object\n");
    printf("  length: %zd\n", size);
    printf("  value: %ls\n", unicode_str);
}

