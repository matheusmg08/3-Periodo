import java.sql.Connection;
import java.sql.DriverManager;

public class ConectaDB {
    //conexao com BD
    //atributo
    private Connection conexao;

    //construtor
    //conecta no Banco de Dados
    public ConectaDB(){
        //url do banco de dados
        String url = "jdbc:mariadb://localhost:3306/ed2";
        String user = "root";
        String pwd = "0207";

        try {
            conexao = DriverManager.getConnection(url, user, pwd);
            System.out.println("Conexão Realizada");
        } catch (Exception e) {
            System.out.println(e.getMessage());
            System.out.println("Nao encontrado drive");
        }
    }

    //metodo para retornar a conexao com o BD
    public Connection getConexaoDB(){
        return conexao;
    }
}