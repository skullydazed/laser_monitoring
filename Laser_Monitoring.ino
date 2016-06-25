// Initialize the values we monitor
int current1_val = 0;
int current2_val = 0;
int current3_val = 0;
int dc_current_val = 0;
int temp1_val = 0;
int temp2_val = 0;

void setup() {
  // Initialize serial communications
  Serial.begin(57600);
}

void loop() {
  // Collect the data
  current1_val = analogRead(A0);
  delay(100);
  current2_val = analogRead(A1);
  delay(100);
  current3_val = analogRead(A2);
  delay(100);
  dc_current_val = analogRead(A3);
  delay(100);
  temp1_val = analogRead(A4);
  delay(100);
  temp2_val = analogRead(A5);

  // Output the data
  Serial.print(current1_val);
  Serial.print('\t');
  Serial.print(current2_val);
  Serial.print('\t');
  Serial.print(current3_val);
  Serial.print('\t');
  Serial.print(dc_current_val);
  Serial.print('\t');
  Serial.print(temp1_val);
  Serial.print('\t');
  Serial.print(temp2_val);
  Serial.print('\n');

  // Wait so this outputs roughly every second
  delay(499);
}
