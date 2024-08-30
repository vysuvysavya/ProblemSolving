class stack {
    Queue < Integer > q = new LinkedList < > ();
    void push(int x) {
        q.add(x);
        for (int i = 0; i < q.size() - 1; i++) {
            q.add(q.remove());
        }
    }
    int pop() {
        return q.remove();
    }
    int top() {
        return q.peek();
    }
    int size() {
        return q.size();
    }
}

=======================================================================

As we know stack follows last in first out, 
  which means we get the most recently inserted element whenever we remove an element from the stack.
  But queue follows first in first out, it means we get that element which we inserted in the starting at each deletion,
  it means if we want to use the queue like a stack we have 
  to arrange elements in the queue such that we get the most recent element at each deletion.

--------------

Take a single queue.
push(x): Push the element in the queue.
Use a for loop of size()-1, remove element from queue and again push back to the queue, hence the most recent element becomes the most former element and vice versa.
pop(): remove the element from the queue.
top(): show the element at the top of the queue.
size(): size of the current queue.
