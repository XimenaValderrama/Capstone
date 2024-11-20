/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package Vista;

import java.awt.Color;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 *
 * @author digim
 */
public class Mascotas_Encontradas extends javax.swing.JFrame {


    public Mascotas_Encontradas() {
        setResizable(false);
        initComponents();
        this.setLocationRelativeTo(null);
        
        Login login = new Login();
        txtUsuario.setText(login.TipoUsuario);
        cargarDatosTabla(); // Llamamos al método para cargar datos de la API en la tabla
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        BTEliminarMasEnCo = new javax.swing.JButton();
        txtUsuario = new javax.swing.JLabel();
        jScrollPane2 = new javax.swing.JScrollPane();
        TablaMascotasAdoptadas = new javax.swing.JTable();
        BTModificarMasEnCo = new javax.swing.JButton();
        BTVolver = new javax.swing.JButton();
        txtNombreMascota = new javax.swing.JTextField();
        txtUsername = new javax.swing.JTextField();
        txtEstadoMascota = new javax.swing.JTextField();
        BTSeleccionarMasEnCo = new javax.swing.JButton();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jPanel1.setBackground(new java.awt.Color(51, 204, 255));

        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 36)); // NOI18N
        jLabel1.setText("Bienvenido:");

        BTEliminarMasEnCo.setText("Eliminar Mascota Encontrada");
        BTEliminarMasEnCo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTEliminarMasEnCoActionPerformed(evt);
            }
        });

        txtUsuario.setFont(new java.awt.Font("Segoe UI", 0, 36)); // NOI18N
        txtUsuario.setText("@NOMBRE ADMIN o Usuario");

        TablaMascotasAdoptadas.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null},
                {null, null, null, null}
            },
            new String [] {
                "ID", "Nombre Mascota", "Dueño", "Estado Mascota"
            }
        ));
        jScrollPane2.setViewportView(TablaMascotasAdoptadas);

        BTModificarMasEnCo.setText("Modificar Mascota Encontrada");
        BTModificarMasEnCo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTModificarMasEnCoActionPerformed(evt);
            }
        });

        BTVolver.setText("Volver");
        BTVolver.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTVolverActionPerformed(evt);
            }
        });

        BTSeleccionarMasEnCo.setText("Seleccionar Mascota Encontrada");
        BTSeleccionarMasEnCo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTSeleccionarMasEnCoActionPerformed(evt);
            }
        });

        jLabel2.setText("Nombre Mascota");

        jLabel3.setText("Dueño");

        jLabel4.setText("Estado Mascota");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(BTVolver)
                        .addGap(72, 72, 72)
                        .addComponent(jLabel1)
                        .addGap(47, 47, 47)
                        .addComponent(txtUsuario)
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(BTEliminarMasEnCo, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 250, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addComponent(BTModificarMasEnCo, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 250, javax.swing.GroupLayout.PREFERRED_SIZE))
                                        .addGap(45, 45, 45))
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                        .addComponent(BTSeleccionarMasEnCo)
                                        .addGap(83, 83, 83))))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addGap(99, 99, 99)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel2)
                                    .addComponent(jLabel3)
                                    .addComponent(jLabel4))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                    .addComponent(txtNombreMascota, javax.swing.GroupLayout.DEFAULT_SIZE, 100, Short.MAX_VALUE)
                                    .addComponent(txtUsername)
                                    .addComponent(txtEstadoMascota))
                                .addGap(65, 65, 65)))
                        .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap())
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(10, 10, 10)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtUsuario)
                            .addComponent(jLabel1)))
                    .addComponent(BTVolver))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(21, Short.MAX_VALUE))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(0, 0, Short.MAX_VALUE)
                        .addComponent(BTSeleccionarMasEnCo)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtNombreMascota, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel2))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtUsername, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel3))
                        .addGap(18, 18, 18)
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtEstadoMascota, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel4))
                        .addGap(18, 18, 18)
                        .addComponent(BTModificarMasEnCo, javax.swing.GroupLayout.PREFERRED_SIZE, 79, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(64, 64, 64)
                        .addComponent(BTEliminarMasEnCo, javax.swing.GroupLayout.PREFERRED_SIZE, 79, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(85, 85, 85))))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void BTVolverActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTVolverActionPerformed
            Menu_Admin Menu_a = new Menu_Admin();
            Menu_a.setVisible(true);
            this.dispose();
    }//GEN-LAST:event_BTVolverActionPerformed

    private void BTModificarMasEnCoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTModificarMasEnCoActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_BTModificarMasEnCoActionPerformed

    private void BTEliminarMasEnCoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTEliminarMasEnCoActionPerformed
     manejarEliminacionMascota();
    }//GEN-LAST:event_BTEliminarMasEnCoActionPerformed

    private void BTSeleccionarMasEnCoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTSeleccionarMasEnCoActionPerformed
        manejarSeleccionMascota(); // Llama al método para manejar la selección del usuario
    }//GEN-LAST:event_BTSeleccionarMasEnCoActionPerformed
  
    private String token = "b0533e8356de17655c128d5fa9a6ca4a0537872d";
    //--------------------------------------------------------INICIO LISTAR DATOS-------------------------------------------------------------------------
private void cargarDatosTabla() {
    String urlString = "http://127.0.0.1:8000/api/mascota/?format=json";
    DefaultTableModel model = (DefaultTableModel) TablaMascotasAdoptadas.getModel();
    model.setRowCount(0); // Limpiar la tabla antes de cargar nuevos datos

    try {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Token " + token);
        connection.connect();

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String inputLine;

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            // Parsear JSON
            JSONArray mascotasArray = new JSONArray(response.toString());
            for (int i = 0; i < mascotasArray.length(); i++) {
                JSONObject mascotaObj = mascotasArray.getJSONObject(i);

                // Obtener el ID y el nombre de la mascota
                int id = mascotaObj.getInt("id");
                String nombreMascota = mascotaObj.optString("nombre", "N/A");
                
                // Obtener el objeto usuario_django
                JSONObject usuario = mascotaObj.optJSONObject("usuario_django");
                String nombreUsuario = "N/A";
                if (usuario != null) {
                    nombreUsuario = usuario.optString("username", "N/A");
                }

                // Obtener el estado de la mascota
                JSONObject estadoMascota = mascotaObj.optJSONObject("estado_mascota");
                String estado = "N/A";
                if (estadoMascota != null) {
                    estado = estadoMascota.optString("descripcion", "N/A");  // Asumiendo que 'descripcion' es el campo dentro de 'estado_mascota'
                }

                // Filtrar solo las mascotas cuyo estado es "Adoptada"
                if (estado.equals("encontrado")) {
                    // Mostrar en consola para depuración
                    System.out.println("ID Mascota: " + id);
                    System.out.println("Nombre Mascota: " + nombreMascota);
                    System.out.println("Dueño: " + nombreUsuario);
                    System.out.println("Estado de la Mascota: " + estado);

                    // Añadir los datos a la tabla solo si la mascota está adoptada
                    model.addRow(new Object[]{id, nombreMascota, nombreUsuario, estado});
                }
            }
        } else {
            JOptionPane.showMessageDialog(this, "Error en la conexión. Código de respuesta: " + responseCode);
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(this, "Error al cargar datos de la API.");
    }
}







//-------------------------------------------------------FIN LISTAR DATOS---------------------------------------------------------------------

//-------------------------------------------------------INICIO ELIMINAR MASCOTA ADOPTADA-----------------------------------------------------
// Método para eliminar una mascota a través de la API
private void eliminarMascota(int mascotaId) {
    String urlString = "http://127.0.0.1:8000/api/mascota/" + mascotaId + "/"; // URL de la API para eliminar

    try {
        // Crear la URL y la conexión
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // Configurar el método DELETE y los encabezados
        connection.setRequestMethod("DELETE");
        connection.setRequestProperty("Authorization", "Token " + token);  // Token de autenticación
        connection.setRequestProperty("Accept", "application/json");

        // Conectar y obtener la respuesta
        connection.connect();
        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_NO_CONTENT) {
            JOptionPane.showMessageDialog(null, "Mascota eliminada correctamente.");
            // Aquí puedes actualizar la tabla o hacer otras acciones
        } else {
            JOptionPane.showMessageDialog(null, "Error al eliminar mascota. Código de respuesta: " + responseCode);
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al eliminar mascota.");
    }
}

// Método común para manejar la eliminación de la mascota
private void manejarEliminacionMascota() {
    // Obtener la fila seleccionada
    int filaSeleccionada = TablaMascotasAdoptadas.getSelectedRow();

    if (filaSeleccionada != -1) {
        // Obtener el ID de la mascota en la primera columna (suponiendo que el ID está en la columna 0)
        int mascotaId = (int) TablaMascotasAdoptadas.getValueAt(filaSeleccionada, 0);

        // Mostrar un cuadro de confirmación para eliminar la mascota
        int confirmacion = JOptionPane.showConfirmDialog(null, 
            "¿Está seguro de que desea eliminar esta mascota?", 
            "Confirmar eliminación", 
            JOptionPane.YES_NO_OPTION);

        if (confirmacion == JOptionPane.YES_OPTION) {
            eliminarMascota(mascotaId); // Llamar al método de eliminación
            cargarDatosTabla();  // Método para recargar la tabla si es necesario
        }
    } else {
        JOptionPane.showMessageDialog(null, "Por favor, seleccione una mascota de la tabla.");
    }
}

// Método para agregar el listener al hacer clic en la fila de la tabla
private void agregarListenerTabla() {
    TablaMascotasAdoptadas.addMouseListener(new MouseAdapter() {
        public void mouseClicked(MouseEvent e) {
            manejarEliminacionMascota(); // Llamar al método común
        }
    });
}

//-------------------------------------------------------FIN ELIMINAR MASCOTA ADOPTADA--------------------------------------------------------

//--------------------------------------------------------INICIO SELECCION MASCOTA ADOPTADA-------------------------------------------------------------
// Método para seleccionar una mascota y cargar sus datos desde la API
private void seleccionarMascota(int mascotaId) {
    String urlString = "http://127.0.0.1:8000/api/mascota/" + mascotaId + "/"; // URL de la API para obtener datos de la mascota

    try {
        // Crear la URL y la conexión
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // Configurar el método GET y los encabezados
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Token " + token);  // Token de autenticación
        connection.setRequestProperty("Accept", "application/json");

        // Conectar y obtener la respuesta
        connection.connect();
        int responseCode = connection.getResponseCode();

        if (responseCode == HttpURLConnection.HTTP_OK) {
            // Leer la respuesta de la API
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            // Convertir la respuesta en un JSONObject
            JSONObject jsonResponse = new JSONObject(response.toString());

            // Procesar estado de la mascota como objeto JSON
            String estadoMascota = "N/A";
            JSONObject estadoMascotaObj = jsonResponse.optJSONObject("estado_mascota");
            if (estadoMascotaObj != null) {
                estadoMascota = estadoMascotaObj.optString("descripcion", "N/A");
            }

            // Filtrar solo si el estado de la mascota es "encontrado"
            if (estadoMascota.equals("encontrado")) {
                // Obtener los datos básicos de la mascota
                String nombreMascota = jsonResponse.optString("nombre", "N/A");
                String username = jsonResponse.optString("username", "N/A");

                // Mostrar los datos en los campos correspondientes
                txtNombreMascota.setText(nombreMascota);
                txtUsername.setText(username);
                txtEstadoMascota.setText(estadoMascota);

                // Deshabilitar los campos que no deben ser modificados
                txtNombreMascota.setEditable(false);
                txtNombreMascota.setBackground(Color.GRAY);

                txtUsername.setEditable(false);
                txtUsername.setBackground(Color.GRAY);

                txtEstadoMascota.setEditable(false);
                txtEstadoMascota.setBackground(Color.GRAY);
            } else {
                JOptionPane.showMessageDialog(null, "La mascota seleccionada no está adoptada.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "Error al obtener datos de la mascota.");
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(null, "Error al seleccionar mascota.");
    }
}

// Método para manejar la selección de la mascota en la tabla y cargar los datos
private void manejarSeleccionMascota() {
    // Obtener la fila seleccionada
    int filaSeleccionada = TablaMascotasAdoptadas.getSelectedRow();

    if (filaSeleccionada != -1) {
        // Obtener el ID de la mascota en la primera columna (suponiendo que el ID está en la columna 0)
        int mascotaId = (int) TablaMascotasAdoptadas.getValueAt(filaSeleccionada, 0);

        // Confirmación de selección
        int confirmacion = JOptionPane.showConfirmDialog(null,
            "¿Está seguro de que desea cargar los datos de esta mascota?",
            "Confirmar selección",
            JOptionPane.YES_NO_OPTION);

        if (confirmacion == JOptionPane.YES_OPTION) {
            seleccionarMascota(mascotaId); // Llamar al método para cargar los datos
        }
    } else {
        JOptionPane.showMessageDialog(null, "Por favor, seleccione una mascota de la tabla.");
    }
}

//--------------------------------------------------------FIN SELECCION MASCOTA ADOPTADA-------------------------------------------------------
    
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Mascotas_Encontradas.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Mascotas_Encontradas.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Mascotas_Encontradas.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Mascotas_Encontradas.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }


        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Mascotas_Encontradas().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BTEliminarMasEnCo;
    private javax.swing.JButton BTModificarMasEnCo;
    private javax.swing.JButton BTSeleccionarMasEnCo;
    private javax.swing.JButton BTVolver;
    private javax.swing.JTable TablaMascotasAdoptadas;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTextField txtEstadoMascota;
    private javax.swing.JTextField txtNombreMascota;
    private javax.swing.JTextField txtUsername;
    private javax.swing.JLabel txtUsuario;
    // End of variables declaration//GEN-END:variables
}
