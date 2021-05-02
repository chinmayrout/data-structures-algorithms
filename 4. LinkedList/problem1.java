// Java program for reversing the linked list
//https://www.youtube.com/watch?v=D7y_hoT_YZI
//https://www.youtube.com/watch?v=njTh_OwMljA
//https://www.youtube.com/watch?v=NhapasNIKuQ

class problem1 {

    static Node head;

    static class Node {

        int data;
        Node next;

        Node(int d) {   //constructor
            data = d;
            next = null;
        }
    }

    

    //Function to reverse the linked list
    static Node reverse(Node node)  //important to differenciate between node and head
    {

        /**
         * Time Complexity: O(n) 
         * Space Complexity: O(1)
         */
        Node prev = null;
        Node current = node;
        Node next = null;

        while(current != null){
            next = current.next;        //learn this!
            current.next = prev;
            prev = current;
            current = next;
        }
        node = prev;
        return node;
    }


   

    //print content of double reversed linked list
    void printList(Node node)
    {
        while(node != null){
            System.out.print(node.data + " ");
            node = node.next;
        }
    }


    static Node recReverse(Node node){
        if(node == null || node.next == null)
            return node;

        //reverse the rest list and put the first element at the end
        Node rest = recReverse(node.next);
        node.next.next = node;

        //tricky step
        node.next = null;

        //fix the head pointer
        return rest; 

    }




    //Driver code
    public static void main(String args[]){
        problem1 llist = new problem1();
        llist.head = new Node(54);
        llist.head.next = new Node(23);
        llist.head.next.next = new Node(4);
        llist.head.next.next.next = new Node(423);

        System.out.println("Given linked List is:");
        llist.printList(head);
        head = llist.reverse(head);
        System.out.println("");
        System.out.println("Reversed linked list! ");
        llist.printList(head);
    }


}