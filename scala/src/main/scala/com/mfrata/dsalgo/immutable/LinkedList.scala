package com.mfrata.dsalgo.immutable

import scala.annotation.tailrec


trait LinkedList[+T] {
  def head: T
  def tail: LinkedList[T]
  def add[S >: T](element: S): LinkedList[S]
  def size: Int
  def index(idx: Int): T
}

case object EmptyList extends LinkedList[Nothing] {
  override def head: Nothing = throw new NoSuchElementException

  override def tail: Nothing = throw new NoSuchElementException

  override def add[S >: Nothing](element: S): LinkedList[S] =
    LList(element, EmptyList)

  override def size: Int = 0

  override def index(idx: Int): Nothing = throw new IndexOutOfBoundsException
}

case class LList[+T](
  override val head: T,
  override val tail: LinkedList[T]
) extends LinkedList[T] {

  override def add[S >: T](element: S): LinkedList[S] = LList(element, this)

  override def size: Int = {
    @tailrec
    def countSize(acc: Int, linkedList: LinkedList[T]): Int = {
      linkedList match {
        case EmptyList => acc
        case _ => countSize(acc + 1, linkedList.tail)
      }
    }
    countSize(1, tail)
  }

  override def index(idx: Int): T = {
    if (idx < 0) EmptyList.index(idx)

    @tailrec
    def findIndex(curIndex: Int, linkedList: LinkedList[T]): T = {
      linkedList match {
        case EmptyList => EmptyList.index(curIndex)
        case _ => if (curIndex == idx) linkedList.head else findIndex(curIndex + 1, linkedList.tail)
      }
    }
    findIndex(0, this)
  }
}

