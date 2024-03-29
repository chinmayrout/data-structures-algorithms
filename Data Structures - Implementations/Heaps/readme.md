### Heaps

## Heaps are advanced data structures that are useful in applications such as sorting and implementing priority queues. They are regular binary trees with two special properties

Heaps must be Complete Binary Trees #
As discussed in the chapter on trees, a Complete Binary tree is a tree where each node has at most two children and the nodes at all levels are full, except for the leaf nodes which can be empty.

Some Complete Binary Tree Properties:

1. All leaves are either at depth dd or depth d-1d−1.
2. The leaves at depth dd are to the left of the leaves at depth d-1d−1
3. There is at most one node with just one child
4. If the singular child exists, it is the left child of its parent
5. If the singular child exists, it is the right most leaf at depth dd.

heappushpop() is equivalent to pushing first, then popping, meaning, amongst other things, that your heap size might change in the process (and that, for example, if your heap is empty you'll get back the element you pushed).

heapreplace() is equivalent to popping first, then pushing, with the additional restriction of guaranteeing that your heap size won't change in the process. this means you'll get an error on an empty heap, amongst other interesting corner behaviour.
