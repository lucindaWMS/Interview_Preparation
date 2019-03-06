public class BSTSet<T> implements set<T> {
	BSTree tree;
	int length;

	class BSTree {
		T val;
		BSTree left, right;

		BSTree add(T val) {
			if(this.val == null) {
				this.val = val;
				return this;
			} else {
				if(this.val.equals(val)) {
					return null;
				} else if (this.val.hashCode() > val.hashCode()) {
					if (this.left == null) {
						this.left = new BSTree();
					}
					return this.left.add(val);
				} else {
					if (this.right == null) {
						this.right = new BSTree();
					}
					return this.right.add(val);
				}
			}
		}

		void add(BSTree tree) {
			if (tree != null && tree.val != null) {
				add(tree.val);
				add(tree.left);
				add(tree.right);
			}
		}

		BSTree find(T val) {
			if (val == null || this.val == null) {
				return null;
			} else if (val.equals(this.val)) {
				return this;
			} else if (val.hashCode() < this.val.hashCode()) {
				return ((this.left == null) ? null : this.left.find(val));
			} else {
				return ((this.right == null) ? null : this.right.find(val));
			}
		}
	}

	public void add (T val) {
		if (this.tree == null) {
			this.tree = new BSTree();
		}
		if (this.tree.add(val) != null) {
			this.length ++;
		}
	}

	public boolean contains(T val) {
		if (this.tree == null) {
			return false;
		} else {
			return this.tree.find(val) != null;
		}
	}

	public int size() {
		return this.length;
	}

	public void remove(T val) {
		BSTree root = this.tree.find(val);
		if (root != null) {
			root.val = null;
			BSTree left = root.left;
			BSTree right = root.right;
			root.left = null;
			root.right = null;
			this.length --;
			this.tree.add(left);
			this.tree.add(right);
		}
	}

	public set<T> newInstance() {
		return null;
	}

	public static void main(String[] args) {
		BSTSet set = new BSTSet();
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