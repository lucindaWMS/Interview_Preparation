public interface set<T> {
	public void add(T val);
	public boolean contains(T val);
	public void remove(T val);
	public int size();
	public set<T> newInstance();
}