using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PongCSharp
{
     public partial class Form1 : Form
     {
          private static float speed = 15;
          private static Random rndInst = new Random();
          private decimal playerScore = 0M;
          private decimal compScore = 0M;
          private Point ballStart = new Point(304, 213);
          private string mBoxPrompt = "Do you want to continue?";
          private DialogResult response = 0;
          private string title = "Pong";
          private float xVel = (float)(Math.Cos(rndInst.Next(5, 10)) * speed);
          private float yVel = (float)(Math.Sin(rndInst.Next(5, 10)) * speed);

          public Form1()
          {
               InitializeComponent();
          }

          private void Form1_Load(object sender, EventArgs e)
          {
               System.Windows.Forms.Cursor.Hide();
          }

          private void BallTimer_Tick(object sender, EventArgs e)
          {
               if (System.Windows.Forms.Cursor.Position.Y > 5 && System.Windows.Forms.Cursor.Position.Y < this.Height - 40 - Ppad.Height)
               {
                    Ppad.Location = new Point(Ppad.Location.X, System.Windows.Forms.Cursor.Position.Y);
               }
               Ball.Location = new Point(Ball.Location.X + (int)xVel, Ball.Location.Y + (int)yVel);
               if (Ball.Bounds.IntersectsWith(Top.Bounds) || (Ball.Bounds.IntersectsWith(Bottom.Bounds)))
               {
                    yVel = -yVel;
               }
               if (Ball.Bounds.IntersectsWith(Cpad.Bounds))
               {
                    xVel = -xVel;
                    Ball.Location = new Point(24, Ball.Location.Y);
               }
               if (Ball.Bounds.IntersectsWith(Ppad.Bounds))
               {
                    xVel = -xVel;
                    Ball.Location = new Point(580, Ball.Location.Y);
               }

               //unbeatable computer paddle
               if (Ball.Location.Y > 5 && Ball.Location.Y < this.Height - 40 - Cpad.Height)
               {
                    Cpad.Location = new Point(Cpad.Location.X, Ball.Location.Y);
               }

               //check if a point is scored, if yes, reset the ball location and
               //check if the game is over
               if (Ball.Bounds.IntersectsWith(Left.Bounds))
               {
                    playerScore += 1;
                    Pscore.Text = playerScore.ToString();
                    Restart();
                    EndGame();
               }
               else if (Ball.Bounds.IntersectsWith(Right.Bounds))
               {
                    compScore += 1;
                    Cscore.Text = compScore.ToString();
                    Restart();
                    EndGame();
               }
          }

          //private void Form1_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
          //{
          //     //make the mouse move
          //     if (e.Y > 5 && e.Y < this.Height - 40 - Ppad.Height)
          //     {
          //          //Ppad.Location = new Point(Ppad.Location.X, e.Y);
          //          Ppad.Location = System.Windows.Forms.Cursor.Position;
          //     }
          //     this.Close();
          //}

          public void Restart()
          {
               //reset only the balls location
               Ball.Location = ballStart;
               rndInst = new Random();
               xVel = (float)(Math.Cos(rndInst.Next(5, 10)) * speed);
               yVel = (float)(Math.Sin(rndInst.Next(5, 10)) * speed);
          }

          public void EndGame()
          {
               //if either score is at 5 the game ends
               if (Pscore.Text.Equals("5"))
               {
                    Label4.Visible = true;
                    System.Windows.Forms.Cursor.Show();
                    Ball.Location = ballStart;
                    BallTimer.Enabled = false;
                    EndMenu();
                    //PlayWinSoundResource();
               }
               else if (Cscore.Text.Equals("5"))
               {
                    Label3.Visible = true;
                    System.Windows.Forms.Cursor.Show();
                    Ball.Location = ballStart;
                    BallTimer.Enabled = false;
                    //PlayLoseSoundResource();
                    EndMenu();
               }
          }

          private void EndMenu()
          {
               //close or reset game with a msg box after the game ends
               response = MessageBox.Show(mBoxPrompt, title, MessageBoxButtons.YesNo);
               if (response == DialogResult.Yes)
               {
                    ResetGame();
               }
               else
               {
                    this.Close();
               }
          }

          private void ResetGame()
          {
               //reset the game
               playerScore = 0;
               compScore = 0;
               Pscore.Text = "0";
               Cscore.Text = "0";
               xVel = (float)(Math.Cos(rndInst.Next(5, 10)) * speed);
               yVel = (float)(Math.Sin(rndInst.Next(5, 10)) * speed);
               Ball.Location = ballStart;
               Label3.Visible = false;
               System.Windows.Forms.Cursor.Hide();
               BallTimer.Enabled = true;
          }
     }
}