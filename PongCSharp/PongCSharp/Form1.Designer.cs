
namespace PongCSharp
{
     partial class Form1
     {
          /// <summary>
          ///  Required designer variable.
          /// </summary>
          private System.ComponentModel.IContainer components = null;

          /// <summary>
          ///  Clean up any resources being used.
          /// </summary>
          /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
          protected override void Dispose(bool disposing)
          {
               if (disposing && (components != null))
               {
                    components.Dispose();
               }
               base.Dispose(disposing);
          }

          #region Windows Form Designer generated code

          /// <summary>
          ///  Required method for Designer support - do not modify
          ///  the contents of this method with the code editor.
          /// </summary>
          private void InitializeComponent()
          {
               this.components = new System.ComponentModel.Container();
               this.Ppad = new System.Windows.Forms.PictureBox();
               this.Cpad = new System.Windows.Forms.PictureBox();
               this.Ball = new System.Windows.Forms.RadioButton();
               this.Label3 = new System.Windows.Forms.Label();
               this.Label4 = new System.Windows.Forms.Label();
               this.Cscore = new System.Windows.Forms.Label();
               this.pictureBox3 = new System.Windows.Forms.PictureBox();
               this.Pscore = new System.Windows.Forms.Label();
               this.BallTimer = new System.Windows.Forms.Timer(this.components);
               this.Top = new System.Windows.Forms.PictureBox();
               this.Bottom = new System.Windows.Forms.PictureBox();
               this.Left = new System.Windows.Forms.PictureBox();
               this.Right = new System.Windows.Forms.PictureBox();
               ((System.ComponentModel.ISupportInitialize)(this.Ppad)).BeginInit();
               ((System.ComponentModel.ISupportInitialize)(this.Cpad)).BeginInit();
               ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).BeginInit();
               ((System.ComponentModel.ISupportInitialize)(this.Top)).BeginInit();
               ((System.ComponentModel.ISupportInitialize)(this.Bottom)).BeginInit();
               ((System.ComponentModel.ISupportInitialize)(this.Left)).BeginInit();
               ((System.ComponentModel.ISupportInitialize)(this.Right)).BeginInit();
               this.SuspendLayout();
               // 
               // Ppad
               // 
               this.Ppad.BackColor = System.Drawing.SystemColors.ButtonHighlight;
               this.Ppad.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
               this.Ppad.Location = new System.Drawing.Point(600, 197);
               this.Ppad.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
               this.Ppad.Name = "Ppad";
               this.Ppad.Size = new System.Drawing.Size(12, 47);
               this.Ppad.TabIndex = 3;
               this.Ppad.TabStop = false;
               // 
               // Cpad
               // 
               this.Cpad.BackColor = System.Drawing.SystemColors.ButtonHighlight;
               this.Cpad.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
               this.Cpad.Location = new System.Drawing.Point(12, 197);
               this.Cpad.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
               this.Cpad.Name = "Cpad";
               this.Cpad.Size = new System.Drawing.Size(12, 47);
               this.Cpad.TabIndex = 4;
               this.Cpad.TabStop = false;
               // 
               // Ball
               // 
               this.Ball.Checked = true;
               this.Ball.Location = new System.Drawing.Point(304, 213);
               this.Ball.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
               this.Ball.Name = "Ball";
               this.Ball.Padding = new System.Windows.Forms.Padding(1);
               this.Ball.Size = new System.Drawing.Size(16, 15);
               this.Ball.TabIndex = 5;
               this.Ball.TabStop = true;
               this.Ball.UseVisualStyleBackColor = true;
               // 
               // Label3
               // 
               this.Label3.AutoSize = true;
               this.Label3.Font = new System.Drawing.Font("Segoe UI", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
               this.Label3.Location = new System.Drawing.Point(66, 202);
               this.Label3.Name = "Label3";
               this.Label3.Size = new System.Drawing.Size(201, 37);
               this.Label3.TabIndex = 10;
               this.Label3.Text = "Computer Wins";
               this.Label3.Visible = false;
               // 
               // Label4
               // 
               this.Label4.AutoSize = true;
               this.Label4.Font = new System.Drawing.Font("Segoe UI", 20F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
               this.Label4.Location = new System.Drawing.Point(377, 202);
               this.Label4.Name = "Label4";
               this.Label4.Size = new System.Drawing.Size(154, 37);
               this.Label4.TabIndex = 11;
               this.Label4.Text = "Player Wins";
               this.Label4.Visible = false;
               // 
               // Cscore
               // 
               this.Cscore.BackColor = System.Drawing.SystemColors.ControlLight;
               this.Cscore.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
               this.Cscore.Font = new System.Drawing.Font("Segoe UI", 17F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
               this.Cscore.Location = new System.Drawing.Point(273, 0);
               this.Cscore.Name = "Cscore";
               this.Cscore.Size = new System.Drawing.Size(40, 40);
               this.Cscore.TabIndex = 12;
               this.Cscore.Text = "00";
               // 
               // pictureBox3
               // 
               this.pictureBox3.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
               this.pictureBox3.Location = new System.Drawing.Point(312, 0);
               this.pictureBox3.Name = "pictureBox3";
               this.pictureBox3.Size = new System.Drawing.Size(1, 440);
               this.pictureBox3.TabIndex = 15;
               this.pictureBox3.TabStop = false;
               // 
               // Pscore
               // 
               this.Pscore.BackColor = System.Drawing.SystemColors.ControlLight;
               this.Pscore.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
               this.Pscore.Font = new System.Drawing.Font("Segoe UI", 17F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point);
               this.Pscore.Location = new System.Drawing.Point(312, 0);
               this.Pscore.Name = "Pscore";
               this.Pscore.Size = new System.Drawing.Size(40, 40);
               this.Pscore.TabIndex = 16;
               this.Pscore.Text = "00";
               // 
               // BallTimer
               // 
               this.BallTimer.Enabled = true;
               this.BallTimer.Interval = 25;
               this.BallTimer.Tick += new System.EventHandler(this.BallTimer_Tick);
               // 
               // Top
               // 
               this.Top.Location = new System.Drawing.Point(0, 0);
               this.Top.Name = "Top";
               this.Top.Size = new System.Drawing.Size(640, 1);
               this.Top.TabIndex = 17;
               this.Top.TabStop = false;
               // 
               // Bottom
               // 
               this.Bottom.Location = new System.Drawing.Point(0, 440);
               this.Bottom.Name = "Bottom";
               this.Bottom.Size = new System.Drawing.Size(640, 1);
               this.Bottom.TabIndex = 18;
               this.Bottom.TabStop = false;
               // 
               // Left
               // 
               this.Left.Location = new System.Drawing.Point(-2, 0);
               this.Left.Name = "Left";
               this.Left.Size = new System.Drawing.Size(1, 440);
               this.Left.TabIndex = 19;
               this.Left.TabStop = false;
               // 
               // Right
               // 
               this.Right.Location = new System.Drawing.Point(625, 0);
               this.Right.Margin = new System.Windows.Forms.Padding(0);
               this.Right.Name = "Right";
               this.Right.Size = new System.Drawing.Size(1, 440);
               this.Right.TabIndex = 20;
               this.Right.TabStop = false;
               // 
               // Form1
               // 
               this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
               this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
               this.BackColor = System.Drawing.SystemColors.ButtonShadow;
               this.ClientSize = new System.Drawing.Size(624, 441);
               this.Controls.Add(this.Right);
               this.Controls.Add(this.Left);
               this.Controls.Add(this.Bottom);
               this.Controls.Add(this.Top);
               this.Controls.Add(this.Pscore);
               this.Controls.Add(this.pictureBox3);
               this.Controls.Add(this.Cscore);
               this.Controls.Add(this.Label4);
               this.Controls.Add(this.Label3);
               this.Controls.Add(this.Cpad);
               this.Controls.Add(this.Ppad);
               this.Controls.Add(this.Ball);
               this.Name = "Form1";
               this.Text = "Form1";
               this.Load += new System.EventHandler(this.Form1_Load);
               ((System.ComponentModel.ISupportInitialize)(this.Ppad)).EndInit();
               ((System.ComponentModel.ISupportInitialize)(this.Cpad)).EndInit();
               ((System.ComponentModel.ISupportInitialize)(this.pictureBox3)).EndInit();
               ((System.ComponentModel.ISupportInitialize)(this.Top)).EndInit();
               ((System.ComponentModel.ISupportInitialize)(this.Bottom)).EndInit();
               ((System.ComponentModel.ISupportInitialize)(this.Left)).EndInit();
               ((System.ComponentModel.ISupportInitialize)(this.Right)).EndInit();
               this.ResumeLayout(false);
               this.PerformLayout();

          }

          #endregion

          internal System.Windows.Forms.PictureBox Ppad;
          internal System.Windows.Forms.PictureBox Cpad;
          internal System.Windows.Forms.RadioButton Ball;
          internal System.Windows.Forms.Label Label3;
          internal System.Windows.Forms.Label Label4;
          private System.Windows.Forms.Label Cscore;
          private System.Windows.Forms.PictureBox pictureBox3;
          private System.Windows.Forms.Label Pscore;
          private System.Windows.Forms.Timer BallTimer;
          private System.Windows.Forms.PictureBox Top;
          private System.Windows.Forms.PictureBox Bottom;
          private System.Windows.Forms.PictureBox Left;
          private System.Windows.Forms.PictureBox Right;
     }
}

