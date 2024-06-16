//import java.util.Scanner;


public class Main {
    public static void main(Integer[] args) {
        Livro obj1 = new Livro("Hércules");
        obj1.setAutor("Matheus Henrique");
        obj1.setAnoPublicacao(1990);
        //System.out.println(obj1);

        Livro obj2 = new Livro("Harry Potter");
        obj2.setAutor("Warner");
        obj2.setAnoPublicacao(1770);
        //System.out.println(obj2);

        Livro obj3 = new Livro("Homem Aranha");
        obj3.setAutor("Marvel");
        obj3.setAnoPublicacao(1998);
        //System.out.println(obj2);

        //instanciar biblioteca
        Biblioteca bib = new Biblioteca();
        bib.inserir(obj1);
        bib.inserir(obj2);
        bib.inserir(obj3);
        //System.out.println(bib);

        bib.listarTodos();

        bib.consultaID(2);

        bib.remover(4);

        bib.listarTodos();

        Usuario user1 = new Usuario("Marcelo");
        user1.setEmail("marcelo@hotmail.com");
        //System.out.println(user1);

        Usuario user2 = new Usuario("Alysson");
        user2.setEmail("alysson@gmail.com");
        //System.out.println(user2);

        Usuario user3 = new Usuario("Ely");
        user3.setEmail("ely@gmail.com");
        //System.out.println(user3);

        //instanciar biblioteca
        Biblioteca user = new Biblioteca();
        user.inserirUsuario(user1);
        user.inserirUsuario(user2);
        user.inserirUsuario(user3);
        //System.out.println(bib);

        user.listarTodosUsuarios();

        user.consultaIDUsuario(2);

        user.removerUsuario(4);

        user.listarTodosUsuarios();




        //int op = 0;
        //Scanner scanner = new Scanner(System.in);
        
        /*do { 
            int escolha = scanner.nextInt();    
            op = menu();

            if (op == 1){
              String nome = scanner.next();
              String autor= scanner.next();
              String anoPublicacao = scanner.next();

              Livro nome = new Livro(nome);


            }
        } while (op != 5);
        
        */
    }
}
