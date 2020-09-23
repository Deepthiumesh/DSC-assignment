{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "n=int(input())\n",
    "ar=[int(input()) for a in range(0,n)]\n",
    "ar.sort()\n",
    "a=0\n",
    "pair=0\n",
    "for b in range(0,n):\n",
    "    if len(ar)==0:\n",
    "        break\n",
    "    else:\n",
    "        b=ar.pop(0)\n",
    "        if a==b:\n",
    "            pair=pair+1\n",
    "            a=\"sit\"\n",
    "        else:\n",
    "            a=b\n",
    "print(pair)"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
