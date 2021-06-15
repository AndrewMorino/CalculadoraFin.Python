using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace P.I___Cadastro_de_Produtos
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void txtNome_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void btnSalvar_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Nome: " + txtNome.Text + "Codigo: "+ txtCodigo.Text + "EAN: "+ txtEan.Text + "Tipo: "+txtTipo.Text + "Quantidade: "+ txtQuantidade.Text + "Custo: "+ txtCusto.Text
                + "Venda: "+ txtVenda.Text + "Estoque: "+ txtEstoque.Text + "Grupo: "+ txtGrupo.Text + "Observações: " + txtObservacoes.Text + "Fabricante: " + txtFabricante.Text +"Marca: "+ txtMarca.Text);
        }

        private void btnLimpar_Click(object sender, EventArgs e)
        {
            txtNome.Text = "";
            txtCodigo.Text = "";
            txtEan.Text = "";
            txtTipo.Text = "";
            txtQuantidade.Text = "";
            txtCusto.Text = "";
            txtVenda.Text = "";
            txtEstoque.Text = "";
            txtGrupo.Text = "";
            txtObservacoes.Text = "";
            txtFabricante.Text = "";
            txtMarca.Text = "";
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
