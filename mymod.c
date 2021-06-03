#include <Python.h>
#include <math.h>

/* Functions of serching inner-coefficient*/
static PyObject *king(PyObject *self, PyObject *args) {
  int orig, bvi, n;
  double result;

  if (!PyArg_ParseTuple(args,"ddd", &orig, &bvi, &n)) {
    return NULL;
  }
  double orig_k = 0.6;
  double bvi_k = 0.4;
  result = 0.00000001 + (double)((orig * orig_k + bvi * bvi_k ) / n);
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
    int *p;
    if (!PyArg_ParseTuple(args,"l", &p)) {
        return NULL;
    }
    result = (double)(150 - 8.3 * p[0] - 6.0 * p[1]- 4.1 * p[2]) / 100;
    return Py_BuildValue("d", result);
}

/* Helping coefficient*/
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
}

/* Probability*/
static PyObject *p(PyObject *self, PyObject *args) {
}