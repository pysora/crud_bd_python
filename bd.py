create database crud_python;

use crud_python;

CREATE TABLE tb_dis(
  idt_disc INT AUTO_INCREMENT PRIMARY KEY,
  sgl_disc VARCHAR(10) NOT NULL,
  nme_disc VARCHAR(50) NOT NULL,
  num_ch_disc INT NOT NULL
);
