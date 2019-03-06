//Simple LinkedList Data Structure
public class IntLinkedList {
	int val;
	IntLinkedList next;

	public IntLinkedList(int val) {
		this.val = val;
	}

	public void add(int val) {
		if (this.next == null) {
			this.next = new IntLinkedList(val);
		} else {
			this.next.add(val);
		}
	}

	public String toString() {
		if (this.next == null) {
			return this.val + "";
		} else {
			return this.val + ", " + this.next;
		}
	}

	public static void main(String[] args) {
		IntLinkedList list = new IntLinkedList(5);
		list.add(3);
		list.add(2);
		list.add(1);
		System.out.println("Here's the list: " + list);
	}
}