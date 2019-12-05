import java.util.*;
class TIC_TAC_TOE
{
    char p[]=new char[2],a[]=new char[9];
    TIC_TAC_TOE()
    {
        for(int i=0;i<9;++i)
            a[i]='-';
    }

    private void display()
    {
        System.out.println("\fWelcome to play TIC-TAC-TOE world\nfor reference to players");
        System.out.println(" ____________________");
        System.out.println("| a[0] | a[1] | a[2] |");
        System.out.println("|______|______|______|");
        System.out.println("| a[3] | a[4] | a[5] |");
        System.out.println("|______|______|______|");
        System.out.println("| a[6] | a[7] | a[8] |");
        System.out.println("|______|______|______|");
    }

    void input()
    {
        System.out.println("Enter X or O for Player1");
        p[0]=Character.toUpperCase(new Scanner(System.in).next().charAt(0));
        assign();
    }

    private void assign()
    {
        switch(p[0])
        {
            case 'X':p[1]='O';
            break;
            case 'O':p[1]='X';
            break;
            default:System.out.println("Invalid Choice!!!");
            input();
            return;
        }
        System.out.println("Player2 choice is "+p[1]);
    }

    private boolean check(int a,char ch)
    {
        int b=a%3;
        int c=0;
        for(int i=1;i<=3;++i,b+=3)
            if(this.a[b]==ch)
                ++c;
        if(c==3)
            return true;
        b=3*(a/3);
        c=0;
        for(int i=1;i<=3;++i,++b)
            if(this.a[b]==ch)
                ++c;
        if(c==3)
            return true;
        c=0;
        if(a%2==0)
        {
            if(a!=4)
            {
                int in;
                if(a%4==0)
                    in=4;
                else
                    in=2;
                b=a%4;
                for(int i=1;i<=3;++i,b+=in)
                    if(this.a[b]==ch)
                        ++c;
                if(c==3)
                    return true;
            }
            else
            {
                b=0;
                for(int i=1;i<=3;++i,b+=4)
                    if(this.a[b]==ch)
                        ++c;
                if(c==3)
                    return true;
                c=0;
                b=2;
                for(int i=1;i<=3;++i,b+=2)
                    if(this.a[b]==ch)
                        ++c;
                if(c==3)
                    return true;
            }
        }
        return false;
    }

    private void printv()
    {
        int x=0;
        for(int i=0;i<3;++i)
        {
            for(int j=0;j<3;++j)
                System.out.print("\t"+a[x++]);
            System.out.println();
        }
    }

    private void startGame()
    {
        Scanner sc=new Scanner(System.in);
        boolean flag=true;
        for(int i=1;i<=9;++i)
        {
            int ind=2-i%2;
            System.out.println("Player"+ind+" Enter the position");
            int pos=sc.nextInt();
            a[pos]=p[ind-1];
            printv();
            if(check(pos,p[ind-1]))
            {
                System.out.println("Player"+ind+" wins");
                flag=false;
                break;
            }
        }
        if(flag)
            System.out.println("None wins");
        System.out.println("Thank you for playing this game");
    }

    public static void main(String args[])
    {
        TIC_TAC_TOE o1=new TIC_TAC_TOE();
        o1.display();
        o1.input();
        o1.startGame();
    }
}