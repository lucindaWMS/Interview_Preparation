public class LinkedList<T> implements List<T> {

	class Node {

		T val;
		Node next;

		public Node(T val, Node next) {
			this.val = val;
			this.next = next;
		}

		public String toString() {
			return "" + this.val + ((this.next != null) ? (" " + this.next.toString()) : "");
		}
	}

	Node first, last;
	int length;

	public void add (T value) {
		Node node = new Node(value, null);
		if (this.first == null) {
			this.first = this.last = node;
		} else {
			this.last.next = node;
			this.last = this.last.next;
		}
		this.length ++;
	}

	public int size() {
		return this.length;
	}

	private Node getNode(Node start, int index) {
		return (index == 0) ? start : getNode(start.next, index - 1);
	}

	public T get(int index) {
		if (index < 0 || index >= this.length) {
			throw new IndexOutOfBoundsException();
		} else {
			return getNode(this.first, index).val;
		}
	}

	public void remove(int index) {
		if (index < 0 || index >= this.length) {
			throw new IndexOutOfBoundsException();
		} 
		if (index == 0) {
			this.first = this.first.next;
			if (this.first == null) {
				this.last = null;
			}
		} else {
			Node prev = getNode(this.first, index - 1);
			prev.next = prev.next.next;
			if (prev.next == null) {
				this.last = prev;
			}
		}
		this.length --;
	}

	private Node recursiveReverseNode(Node node) {
		if (node.next == null) {
			return node;
		} else {
			Node prev = node.next;
			Node newStart = recursiveReverseNode(node.next);
			prev.next = node;
			return newStart;
		}
	}

	public void reverse() {
		if (this.first != null) {
			this.last = this.first;
			this.first = recursiveReverseNode(this.first);
			this.last.next = null;
		}
	}

	public String toString() {
		if (first == null) {
			return "";
		} else {
			return first.toString();
		}
	}

	public static void main(String[] args) {
		LinkedList<Integer> list = new LinkedList();
		System.out.println("The size is: " + list.size());
		list.add(1);
		list.add(2);
		System.out.println("The size is: " + list.size());
		list.add(4);
		list.add(8);
		System.out.println("The size is: " + list.size());
		list.get(0);
		list.remove(0);
		System.out.println("The size is: " + list.size());
		list.reverse();
		System.out.println("The list is: " + list);
	}
}