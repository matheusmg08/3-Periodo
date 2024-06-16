public class MainDB {
    public static void main(String[] args) {
        Livro liv = new Livro("O senhor dos anéis");
        liv.setAutor("J. R. R. Tolkien");
        liv.setAnoPublicacao(1953);

        Livro liv2 = new Livro("O mágico de Oz");
        liv2.setAutor("L. M. M. Carlos");
        liv2.setAnoPublicacao(1900);


        LivroDao objDAO = new LivroDao();
        objDAO.inserir(liv);

        LivroDao objDAO2 = new LivroDao();
        objDAO2.inserir(liv2);

        

        Usuario user = new Usuario("Matheus");
        user.setEmail("matheus@gmail.com");

        Usuario user2 = new Usuario("Marcelo");
        user2.setEmail("marcelo@hotmail.com");

        UsuarioDao userDao = new UsuarioDao();
        userDao.inserir(user);

        UsuarioDao useDao = new UsuarioDao();
        useDao.inserir(user2);

        }        
    }
