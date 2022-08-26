#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int y;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->alloacted);
	for (y = 0; y < size; y++)
		printf("Element %y: %s\n", y, Py_TYPE(obj->ob_item[y])->tp_name);
}
