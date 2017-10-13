#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <openssl/md5.h>

unsigned char digest[MD5_DIGEST_LENGTH];
const char alphabet[] =
"abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"0123456789";
const int alphabet_size = sizeof(alphabet) - 1;
char* match;

void check(unsigned char* string)
{
	MD5(string, strlen(string), (unsigned char*)&digest);

	match=strstr(digest,"'||'");
	if(match==NULL)
	{
		match=strcasestr(digest,"'or'");
	}
	if(match != NULL && match[4] > '0' && match[4] <= '9')
	{
		printf("%s\n",string);
		printf("%s",digest);
	}
}


void brute_impl(char * str, int index, int max_depth)
{
    for (int i = 0; i < alphabet_size; ++i)
    {
        str[index] = alphabet[i];
        if (index == max_depth - 1)
        {
			check((unsigned char*)str);
		}
        else
        {
            brute_impl(str, index + 1, max_depth);
        }
    }
}

void brute_sequential(int max_len)
{
    char * buf = malloc(max_len + 1);
    for (int i = 1; i <= max_len; ++i)
    {
        memset(buf, 0, max_len + 1);
        brute_impl(buf, 0, i);
    }
    free(buf);
}

int main()
{
	brute_sequential(5);
	return 0;
}