public class factorial {
    

    static int fact(int n){ //non-tail
        if(n == 0 ) return 1;

        return n*fact(n-1);
    }

    static int factTR(int n, int a){
        if(n == 0)
            return a;

        return factTR(n-1, n * a);

    }

    static int fact1(int n){    //tail-recursive; https://www.geeksforgeeks.org/tail-recursion/
        return factTR(n ,1);
    }


    public static void main(String args[]){
        System.out.println(fact(5));
        System.out.println(fact1(6));
    }

}
