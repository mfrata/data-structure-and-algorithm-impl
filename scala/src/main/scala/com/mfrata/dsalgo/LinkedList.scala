package com.mfrata.dsalgo

import scala.annotation.tailrec

final class LinkedList[T](
  initialHead: Option[T] = None,
  initialTail: Option[LinkedList[T]] = None
) {

  var head: Option[T] = initialHead
  var tail: Option[LinkedList[T]] = initialTail
  private var cachedSize: Int = 0

  def add(v: T): Unit = {
    tail = Some(new LinkedList(head, tail))
    head = Some(v)
    cachedSize += 1
  }

  @tailrec
  def find(v: T): Boolean = (head, tail) match {
    case (Some(h), _) if h == v => true
    case (Some(_), Some(tail)) => tail.find(v)
    case _ => false
  }

  def size: Int = cachedSize

  def pop(v: T): Option[T] = (head, tail) match {
    case (Some(h), _) if h == v => {
      head = tail.flatMap(_.head)
      tail = tail.flatMap(_.tail)
      cachedSize -= 1
      Some(v)
    }
    case (Some(_), Some(tail)) => tail.pop(v)
    case _ => None
  }
}
