"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Estructura que contiene la información a guardar en una lista encadenada
"""

def newSingleNode (element):
  """
  Estructura que contiene la información a guardar en una lista encadenada
  Args:
    Element
      Elemento que se desea almacenar en el nodo creado
  Return
    Nodo con la información que se suministra por parámetro
  """
  node = {'info':element,'next':None}
  return (node)



def getElement (node):
  """
  Estructura que contiene la información a guardar en una lista encadenada
  Args:
    Node
      Nodo del cual se desea saber su contenido
  Return
    Elemento dentro del nodo pasado por parametro
  """
  return node ['info']


def newDoubleNode (element):
  """
  Estructura que contiene la información a guardar en una lista encadenada doblemente
  Args::
    element
      Elemento que se desea agregar al nodo
  Return
    Nodo con las posibilidad de doble encadenación (Disponibilidad de añadir nodos antes y despues)
  """
  node = {'info':element,'next':None, 'prev':None}
  return (node)
