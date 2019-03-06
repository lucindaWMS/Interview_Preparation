public class arrayList<T> implements List<T>{

	T[] values = (T[]) new Object[3];
	int length = 0;

	public void add(T val) {
		if (this.length == this.values.length) {
			T[] temp = (T[]) new Object[this.length * 2];
			for (int i = 0; i < this.length; i++) {
				temp[i] = this.values[i];
			}
			this.values = temp;
		}
		this.values[this.length] = val;
		this.length ++;
	}
	
	public void remove(int index) {
		if (index >= this.length || index < 0) {
			throw new IndexOutOfBoundsException();
		} else {
			this.length --;
			for (int i = index; i < this.length; i++) {
				this.values[i] = this.values[i+1];
			}
		}

	}

	public T get(int index) {
		if (index >= this.length || index < 0) {
			throw new IndexOutOfBoundsException();
		} else {
			return this.values[index];
		}
	}

	public int size() {
		return this.length;
	}

	public void reverse() {
		for (int i = 0; i < this.length/2; i++) {
			T tmp = this.values[i];
			this.values[i] = this.values[this.length - i - 1];
			this.values[this.length - i - 1] = tmp;
		}
	}

	public String toString() {
		String res = "";
		for (int i = 0; i < this.size(); i++) {
			res += ((i != 0) ? " " : "") + this.values[i];
		}
		return res;
	}

	public static void main(String[] args) {
		arrayList<Integer> list = new arrayList();
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