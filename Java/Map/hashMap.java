import java.util.LinkedList;

public class hashMap<K, V> implements map<K, V> {
	Object[] table;
	int length;
	private final static int DEFAULT_SIZE = 3;

	public hashMap() {
		this.table = new Object[DEFAULT_SIZE];
	}

	public hashMap(int size) {
		this.table = new Object[size];
	}

	public int hash(K key) {
		return Math.abs(key.hashCode()) % DEFAULT_SIZE;
	}

	class KVPair {
		K key;
		V val;

		KVPair(K key, V val) {
			this.key = key;
			this.val = val;
		}
	}

	private KVPair find(LinkedList<KVPair> list, K key) {
		for (KVPair kv : list) {
			if (kv.key.equals(key)) {
				return kv;
			}
		}
		return null;
	}

	public void put(K key, V val) {
		int value = hash(key);
		if (this.table[value] == null) {
			this.table[value] = new LinkedList<KVPair>();
		}
		LinkedList<KVPair> list = (LinkedList<KVPair>) this.table[value];
		KVPair kv = find(list, key);
		if (kv == null) {
			list.add(new KVPair(key, val));
			this.length ++;
		} else {
			kv.val = val;
		}
	}

	public int size() {
		return this.length;
	}

	public V get (K key) {
		int value = hash(key);
		if (this.table[value] == null) {
			return null;
		} else {
			LinkedList<KVPair> list = (LinkedList<KVPair>) this.table[value];
			KVPair kv = find(list, key);
			if (kv != null) {
				return kv.val;
			} else {
				return null;
			}
		}
	}

	public void remove(K key) {
		int value = hash(key);
		if (this.table[value] != null) {
			LinkedList<KVPair> list = (<LinkedList<KVPair>) this.table[value];
			KVPair kv = find(list, key);
			if (kv != null) {
				list.remove(kv);
				this.length --;
			}
		}
	}
}