#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <string.h>
#include <tchar.h>

int main(int argc, char *argv[])
{
    FILE * fp;
    char pri[255];
    char * word;
    fp = fopen(argv[1], "r");
    if(fp == NULL)
    {
        printf("Error, Cannot Open File\n");
        exit(2);
    }
    while(fgets(pri, 255, fp)){
        word = strtok(pri, " ");
        if (word != NULL)
        {
            
           char cmd[255];
           strcpy(cmd, word);
           word = strtok(NULL, "\n");
           if(strcmp(cmd, "echo") == 0)
           {
            printf("%s\n", word);
           }
           if(strcmp(cmd, "start") == 0)
           {       

            STARTUPINFOA si = {0};
            PROCESS_INFORMATION pi = {0};

            if(ShellExecute(NULL, "open", word, NULL, NULL, SW_SHOWDEFAULT) == 0)
                printf("There was an error, error number\n");
              
           }  
           if(strcmp(cmd, "sudo") == 0)
           {       

            STARTUPINFOA si = {0};
            PROCESS_INFORMATION pi = {0};

            if(ShellExecute(NULL, "runas", word, NULL, NULL, SW_SHOWDEFAULT) == 0)
                printf("There was an error, error number\n");
              
           }  
           if(strcmp(cmd, "cmd") == 0)
           {       
            system(word);
              
           } 
           if(strcmp(cmd, "msgbox") == 0)
           {       
            if(MessageBox(NULL, word, "WinScript", MB_OKCANCEL | MB_ICONQUESTION) != IDOK)
            {
                exit(0);

            }

              
           }     
            if(strcmp(cmd, "msgbox") == 0)
           {       
            if(MessageBox(NULL, word, "WinScript", MB_OKCANCEL | MB_ICONQUESTION) != IDOK)
            {
                exit(0);

            }

              
           }  
           if(strcmp(cmd, "about") == 0)
           {       
            if(MessageBox(NULL, "WinScript Version 0.1 Beta\nMade By zvqle\ngithub.com\\realzvqle\nyoutube.com\\zvqle\n", "WinScript", MB_OKCANCEL | MB_ICONQUESTION) != IDOK)
            {
                exit(0);

            }

              
           }  
        }


    }

    fclose(fp);


    
}
