public class Usuario {
    private int id_usuario;
    private String nome;
    private String email;
    private static int contador2 = 0;

    public Usuario(String nome){
        this.setNome(nome);
        contador2 ++;
        this.setId2(contador2);
    }

    public void setId2(int contador){
        this.id_usuario = contador;
    }

    private void setNome(String nome){
        nome = nome.toUpperCase();
        this.nome = nome;
    }

    public int getId_usuario() {
        return id_usuario;
    }

    public void setId_usuario(int id_usuario) {
        this.id_usuario = id_usuario;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public static int getContador2() {
        return contador2;
    }

    public static void setContador2(int contador2) {
        Usuario.contador2 = contador2;
    }

    //criar toString 
    public String toString(){
        return "ID: " + getId_usuario() + " Nome: " + getNome() + " Email: " + getEmail();
    }   
}
