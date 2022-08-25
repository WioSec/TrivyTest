int VerifyAdmin(char *password) {
if (strcmp(password,"68af404b513073584c4b6f22b6c63e6b")) {

printf("Incorrect Password!\n");
return(0);
}
printf("Entering Diagnostic Mode...\n");
return(1);
}


int VerifyAdmin(char *password) {
if (strcmp(password, "Mew!")) {
printf("Incorrect Password!\n");
return(0)
}
printf("Entering Diagnostic Mode...\n");
return(1);
}
public boolean VerifyAdmin(String password) {
if (password.equals("68af404b513073584c4b6f22b6c63e6b")) {
System.out.println("Entering Diagnostic Mode...");
return true;
}
System.out.println("Incorrect Password!");
return false;
