import org.scalatest.flatspec.AnyFlatSpec

import com.mfrata.dsalgo.immutable.{LList, EmptyList}


class ImutableLinkedListTest extends AnyFlatSpec {
  it should "instantiate EmptyList" in {
    val ll = EmptyList

    intercept[NoSuchElementException] {
      ll.head
    }

    intercept[NoSuchElementException] {
      ll.tail
    }

    assert(ll.size == 0)
  }

  it should "add element 4" in {
    val ll = EmptyList add 4

    assert(ll.head == 4)
    assert(ll.tail == EmptyList)
    assert(ll.size == 1)
  }

  val llist = LList(10, LList(20, LList(30, LList(40, LList(5, EmptyList)))))

  it should "have size 10" in {
    assert(llist.size == 5)
  }

  it should "return 4 on index 5" in {
    assert(llist.index(4) == 5)
  }

  it should "raise index out of bounds when access index greater than size" in {
    intercept[IndexOutOfBoundsException] {
      llist.index(10)
    }
  }

  it should "raise index out of bounds when arg is negative" in {
    intercept[IndexOutOfBoundsException] {
      llist.index(-1)
    }
  }
}
