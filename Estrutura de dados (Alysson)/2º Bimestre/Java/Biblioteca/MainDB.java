
import java.util.Scanner;

public class MainDB {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LivroDao objDao = new LivroDao();
        UsuarioDao userDao = new UsuarioDao();
        
        while (true) {
            System.out.println("Menu:");
            System.out.println("1. Inserir livro");
            System.out.println("2. Inserir usuário");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // Consumir a nova linha

            if (opcao == 1) {
                System.out.print("Digite o título do livro: ");
                String titulo = scanner.nextLine();
                System.out.print("Digite o autor do livro: ");
                String autor = scanner.nextLine();
                System.out.print("Digite o ano de publicação do livro: ");
                int anoPublicacao = scanner.nextInt();
                scanner.nextLine(); // Consumir a nova linha
                    
                Livro liv = new Livro(titulo);
                liv.setAutor(autor);
                liv.setAnoPublicacao(anoPublicacao);
                objDao.inserir(liv);
                    
                System.out.println("Livro inserido com sucesso!");
                    
            }else if(opcao == 2){
                System.out.print("Digite o nome do usuário: ");
                String nome = scanner.nextLine();
                System.out.print("Digite o email do usuário: ");
                String email = scanner.nextLine();
                    
                Usuario user = new Usuario(nome);
                user.setEmail(email);
                userDao.inserir(user);
                    
                System.out.println("Usuário inserido com sucesso!");
                    
            }else if (opcao ==3){ 
                System.out.println("Saindo...");
                scanner.close();
                return;
            }else{   
                System.out.println("Opção inválida. Tente novamente.");
                break;
            }                
        }
    }
}