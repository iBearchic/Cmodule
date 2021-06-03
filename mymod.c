#include <Python.h>
#include <math.h>

/* Functions of serching inner-coefficient*/
static PyObject *king(PyObject *self, PyObject *args) {
  int orig, bvi, n;
  double result;

  if (!PyArg_ParseTuple(args,"iii", &orig, &bvi, &n)) {
    return NULL;
  }
  double orig_k = 0.6;
  double bvi_k = 0.4;
  result = 0.0001 + (double)((orig * orig_k + bvi * bvi_k ) / n);
  return Py_BuildValue("d", result);
}

/* Functions of serching outer-coefficient*/
static PyObject *kong(PyObject *self, PyObject *args) {
    double kp, ko, kd, result;
    if (!PyArg_ParseTuple(args,"ddd", &kp, &ko, &kd)) {
        return NULL;
    }
    result = pow((kp * kd), ko);
    return Py_BuildValue("d", result);
}

/* Partition coefficient*/
static PyObject *kp(PyObject *self, PyObject *args) {
    double result;
    PyObject* p;
    if (!PyArg_ParseTuple(args,"O", &p)) {
        return NULL;
    }
    PyObject* p0 = PySequence_Fast_GET_ITEM(p, 0);
    PyObject* p1 = PySequence_Fast_GET_ITEM(p, 1);
    PyObject* p2 = PySequence_Fast_GET_ITEM(p, 2);

    int res0 = PyLong_AsLong(p0);
    int res1 = PyLong_AsLong(p1);
    int res2 = PyLong_AsLong(p2);

    result = (double)(150 - 8.3 * res0 - 6.0 * res1 - 4.1 * res2) / 100;
    return Py_BuildValue("d", result);
}

/* Helping coefficient
static PyObject *kd(PyObject *self, PyObject *args) {
    int n;
    int *lst;
    if (!PyArg_ParseTuple(args,"dl", &n, &lst)) {
        return NULL;
    }
    double temp = 1.0;
    for(int i = 0, i < n, i++)
    {
        temp = temp - king(lst[i][0][0], lst[i][0][1], 25);
    }
    temp = temp * 1.001203200114052001;
    return Py_BuildValue("d", temp);
}*/

static PyMethodDef ownmod_methods[] = {
    { 
        "king", // name of fucntion in python interpreter
        king, // function C declaration
        METH_VARARGS, // special macros about function arguments
        "Functions of serching inner-coefficient" // doc for function in python interpreter
    },
    { 
        "kong", // name of fucntion in python interpreter
        kong, // function C declaration
        METH_VARARGS, // special macros about function arguments
        "Functions of serching outer-coefficient" // doc for function in python interpreter
    },
    { 
        "kp", // name of fucntion in python interpreter
        kp, // function C declaration
        METH_VARARGS, // special macros about function arguments
        "Partition coefficient" // doc for function in python interpreter
    },
    { NULL, NULL, 0, NULL }
};

static PyModuleDef simple_module = {
    /* Info about module */
    PyModuleDef_HEAD_INIT,
    "my_mod", // my_mod.__name__ 
    "amazing documentation", // my_mod.__doc__ 
    -1, 
    ownmod_methods, // methods are here 
    NULL, 
    NULL, 
    NULL, 
    NULL, 
    NULL
};

PyMODINIT_FUNC PyInit_my_mod(void)
{
    PyObject* m;
    // creating module object
    m = PyModule_Create(&simple_module);
    if (m == NULL)
        return NULL;

    return m;
}
