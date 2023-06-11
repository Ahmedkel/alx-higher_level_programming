#include <Python.h>

/**
 * print_python_list_info - prints some basic info about a Python list
 * @p: pointer to the Python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyUnicode_Check(item))
			printf("str\n");
		else if (PyLong_Check(item))
			printf("int\n");
		else if (PyFloat_Check(item))
			printf("float\n");
		else if (PyList_Check(item))
			printf("list\n");
		else if (PyTuple_Check(item))
			printf("tuple\n");
		else if (PyDict_Check(item))
			printf("dict\n");
		else if (PyAnySet_Check(item))
			printf("set\n");
		else if (PyAnyIterator_Check(item))
			printf("iter\n");
		else if (PyModule_Check(item))
			printf("module\n");
		else if (PyCallable_Check(item))
			printf("function\n");
		else
			printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
