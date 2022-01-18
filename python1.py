{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the value of a: 25\n",
      "Enter the value of b: 45\n",
      "Enter the value of c: 56\n",
      "56 is maximum\n"
     ]
    }
   ],
   "source": [
    "a = eval(input('Enter the value of a: '))\n",
    "b = eval(input('Enter the value of b: '))\n",
    "c = eval(input('Enter the value of c: '))\n",
    "if a>=b:\n",
    "    if a>=c:\n",
    "        print('{} is maximum'.format(a))\n",
    "    else:\n",
    "        print('{} is maximum'.format(c))\n",
    "elif b>=c:\n",
    "    print('{} is maximum'.format(b))\n",
    "else:\n",
    "    print('{} is maximum'.format(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
