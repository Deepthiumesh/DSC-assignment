{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "thriller=[\"Dark\",\"Mindhunter\",\"Parasite\",\"Inception\",\"Insidious\",\"Interstellar\",\"Prison Break\",\"Money Heist\",\"War\",\"Jack Ryan\"]\n",
    "comedy=[\"Friends\",\"3 Idiots\",\"Brooklyn 99\",\"How I Met Your Mother\",\"Rick And Morty\",\"The Big Bang Theory\",\"The Office\",\"Space Force\"]\n",
    "\n",
    "thriller1=(a.lower() for a in thriller)\n",
    "comedy1=(a.lower() for a in comedy)\n",
    "\n",
    "ans=input()\n",
    "\n",
    "if ans.lower() in thriller1:\n",
    "    print(\"It is a thriller\")\n",
    "elif ans.lower() in comedy1:\n",
    "    print(\"It is a comedy\")\n",
    "else:\n",
    "    print(\"It's neither comedy nor thriller\")"
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
