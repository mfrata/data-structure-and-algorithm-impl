import org.scalatest.flatspec.AnyFlatSpec

import com.mfrata.dsalgo.LinkedList


class LinkedListTest extends AnyFlatSpec {
  "LinkedList" should "instantiate with size 0" in {
    val ll = new LinkedList[Int]
    assert(ll.size == 0)
  }

  it should "add value 5" in {
    val ll = new LinkedList[Int]
    ll.add(5)

    assert(ll.head.get == 5)
    assert(ll.tail.get.tail == None)
    assert(ll.size == 1)
  }

  it should "add value 3 and 4" in {
    val ll = new LinkedList[Int]
    Seq(3, 4).map(ll.add)

    assert(ll.head.get == 4)
    assert(ll.tail.get.head.get == 3)
    assert(ll.tail.get.tail.get.tail == None)
    assert(ll.size == 2)
  }

  it should "find value 10" in {
    val ll = new LinkedList[Int]
    Seq(10, 4, 5, 6).map(ll.add)

    assert(ll.find(10) == true)
  }

  it should "not find 10 on empty list" in {
    val ll = new LinkedList[Int]

    assert(ll.find(10) == false)
  }

  it should "not find 10 on list" in {
    val ll = new LinkedList[Int]
    Seq(11, 4, 5, 6).map(ll.add)

    assert(ll.find(10) == false)
  }

  it should "not pop 10 off list" in {
    val ll = new LinkedList[Int]
    Seq(11, 4, 5, 6).map(ll.add)

    assert(ll.size == 4)

    assert(ll.pop(10) == None)
    assert(ll.size == 4)
  }

  it should "pop 4 off the list" in {
    val ll = new LinkedList[Int]
    Seq(11, 4, 5, 6).map(ll.add)

    assert(ll.size == 4)

    assert(ll.pop(4).get == 4)
    assert(ll.size == 4)

    assert(ll.head.get == 6)
    assert(ll.tail.get.head.get == 5)
    assert(ll.tail.get.tail.get.head.get == 11)
  }
}
