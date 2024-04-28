#include <stdio.h>

int arr[51];
int brr[51];

void left(int n)
{
	int i;
	int tmp;
	tmp= arr[0];
	for (i=0;i<n;i++) 
		arr[i]=arr[i+1];
	arr[n-1]=tmp;
}

void right(int n)
{
	int i;
	int tmp;
	tmp= arr[n-1];
	for (i=0;i<n;i++)
		arr[n-i-1]=arr[n-i-2];
	arr[0]=tmp;
}

int main ()
{
	int n,m;
	int i=0,t;
	int j=0,cnt=0;
	int k=0;
	scanf("%d %d",&n,&m);
	for(i=0;i<m;i++){
    scanf("%d",&brr[i]);
  }
  t=n;
	for(i=0;i<n;i++){
    arr[i]=i+1;
  }

	while (1)
	{
		while (brr[j]!=arr[0]) 
		{
			if(brr[j]!=0)
			{
				for (i=0;i<t;i++)
				{
					if(brr[j]==arr[i])
					{
						k=i;break;
					}
				}
				if(k>t/2) {
          right(t);
          cnt++;
          }
				else{
        left(t);
        cnt++;
        }
			}
		}
		arr[0] = 0;
		left(t);
		t--;
    j++;
			if(brr[j]==0) 
				break;
	}

	printf("%d\n",cnt);

	return 0;
}