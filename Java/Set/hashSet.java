import java.util.LinkedList;

public class hashSet<T> implements set<T> {
	Object[] table;
	int length = 0;
	private final static int DEFAULT_SIZE = 3;

	public hashSet() {
		table = new Object[DEFAULT_SIZE];
	}

	public hashSet(int size) {
		table = new Object[size];
	}
 
	public int hash(T val) {
		return Math.abs(val.hashCode()) % DEFAULT_SIZE;
	}

	public void add (T val) {
		int value = hash(val);
		if (table[value] == null) {
			table[value] = new LinkedList<T>();
		}
		LinkedList<T> list = (LinkedList<T>)table[value];
		if (!list.contains(val)) {
			list.add(val);
			this.length ++;
		}
	}

	public int size() {
		return this.length;
	}

	public boolean contains(T val) {
		int value = hash(val);
		return (table[value] != null && ((LinkedList<T>)table[value]).contains(val));
	}

	public void remove(T val) {
		if (contains(val)) {
			int value = hash(val);
			if (table[value] != null) {
				LinkedList<T> list = (LinkedList<T>)table[value];
				if (list.contains(val)) {
					list.remove(val);
					this.length --;
				}
			}
		}
	}

	public set<T> newInstance() {
		return null;
	}

	public static void main(String[] args) {
		hashSet<Integer> set = new hashSet();
		System.out.println("The size is: " + set.size());
		set.add(1);
		set.add(2);
		System.out.println("The size is: " + set.size());
		set.add(4);
		System.out.println("The size is: " + set.size());
		set.add(4);
		System.out.println(set.contains(5));
		set.remove(1);
		System.out.println("The size is: " + set.size());
	}
}