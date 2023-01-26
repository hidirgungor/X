HTML:

<html>
  <head>
    <title>Kazananlar Listesi</title>
  </head>
  <body>
    <h1>Kazananlar Listesi</h1>
    <form action="kazananlar.php" method="post">
      <label for="tc_num">TC Kimlik Numarası:</label>
      <input type="text" id="tc_num" name="tc_num">
      <input type="submit" value="Ara">
    </form>
    <table>
      <tr>
        <th>TC Kimlik Numarası</th>
        <th>Kazandı</th>
      </tr>
      <?php
        if(isset($_POST['tc_num'])) {
          $tc_num = $_POST['tc_num'];
          // Veritabanı bağlantısı kurulur
          $conn = mysqli_connect("host", "kullanici_adi", "parola", "veritabani");
          // TC kimlik numarasına göre arama yapılır
          $query = "SELECT * FROM kazananlar WHERE tc_num = '$tc_num'";
          $result = mysqli_query($conn, $query);
          if(mysqli_num_rows($result) > 0) {
            $row = mysqli_fetch_assoc($result);
            echo "<tr>";
            echo "<td>" . $row['tc_num'] . "</td>";
            if($row['kazandi'] == 1) {
              echo "<td>Evet</td>";
            } else {
              echo "<td>Hayır</td>";
            }
            echo "</tr>";
          } else {
            echo "<tr>";
            echo "<td colspan='2'>Aradığınız TC kimlik numarası ile eşleşen bir kayıt bulunamadı.</td>";
            echo "</tr>";
          }
        }
      ?>
    </table>
  </body>
</html>
Python:

import mysql.connector

Veritabanı bağlantısı kurulur
conn = mysql.connector.connect(
host="host",
user="kullanici_adi",
password="parola",
database="veritabani"
)

cursor = conn.cursor()

TC kimlik numarası alınır
tc_num = input("TC Kimlik Numarası: ")

TC kimlik numarasına göre arama yapılır
query = "SELECT * FROM kazananlar WHERE tc_num = %s"
cursor.execute(query, (tc_num,))

results = cursor.fetchall()

if cursor.rowcount > 0:
for result in results:
print("TC Kimlik Numarası: " + result[0])
if result[1] == 1:
print("Kazandı: Evet")