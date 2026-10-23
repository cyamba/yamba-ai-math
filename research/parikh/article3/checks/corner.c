/* Exact test of corner independence for a window content c_0..c_r.
   Enumerates every tuple of edge projections (Ferrers matrices; each is realised by a word),
   computes every entry E_{i,l}, and checks whether two tuples agree on all entries other than
   the corner E_{0,r} but differ there. Prints INDEPENDENT with a witness, or DETERMINED.
   Usage: ./corner c0 c1 ... cr        (all c_i <= 8, r <= 9) */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#define MAXL 10
#define MAXC 8
static int r, c[MAXL+1];
static int nproj[MAXL]; static int proj[MAXL][200][MAXC]; /* lambda lists per edge */
static int choice[MAXL];
static uint64_t ent[MAXL+1][MAXL+1];
typedef struct { uint64_t h1, h2; uint64_t corner; int used; int ch[MAXL]; } slot;
static slot *tab; static uint64_t tabsize; static long long ndistinct=0, nleaves=0;
static void gen(int e, int pos, int lo, int *cur){
  if(pos==c[e+1]){ memcpy(proj[e][nproj[e]], cur, sizeof(int)*MAXC); nproj[e]++; return; }
  for(int v=lo; v<=c[e]; v++){ cur[pos]=v; gen(e,pos+1,v,cur); }
}
static uint64_t mix(uint64_t x){ x^=x>>33; x*=0xff51afd7ed558ccdULL; x^=x>>33; x*=0xc4ceb9fe1a85ec53ULL; x^=x>>33; return x; }
static uint64_t vec[MAXL+1][MAXL+1][MAXC]; /* vec[start][letter][copy] */
static void leaf(void){
  nleaves++;
  uint64_t h1=0x12345, h2=0x6789;
  for(int i=0;i<=r;i++) for(int l=i;l<=r;l++){ if(i==0&&l==r) continue;
    h1=mix(h1^ent[i][l]^((uint64_t)(i*31+l)<<40)); h2=mix(h2+ent[i][l]*1000003ULL+(uint64_t)(i*17+l)); }
  uint64_t k=h1%tabsize;
  while(tab[k].used){
    if(tab[k].h1==h1 && tab[k].h2==h2){
      if(tab[k].corner!=ent[0][r]){
        printf("INDEPENDENT: corner %llu vs %llu\n",(unsigned long long)tab[k].corner,(unsigned long long)ent[0][r]);
        printf("  witness A lambdas:"); for(int e=0;e<r;e++){printf(" [");for(int s=0;s<c[e+1];s++)printf("%d",proj[e][tab[k].ch[e]][s]);printf("]");} printf("\n");
        printf("  witness B lambdas:"); for(int e=0;e<r;e++){printf(" [");for(int s=0;s<c[e+1];s++)printf("%d",proj[e][choice[e]][s]);printf("]");} printf("\n");
        exit(0);
      }
      return;
    }
    k=(k+1)%tabsize;
  }
  tab[k].used=1; tab[k].h1=h1; tab[k].h2=h2; tab[k].corner=ent[0][r]; memcpy(tab[k].ch,choice,sizeof(choice)); ndistinct++;
}
static void dfs(int e){ /* choose edge e between letters e and e+1 */
  if(e==r){ leaf(); return; }
  for(int p=0;p<nproj[e];p++){
    choice[e]=p; int *lam=proj[e][p];
    for(int i=0;i<=e;i++){
      uint64_t pre[MAXC+1]; pre[0]=0;
      for(int t=0;t<c[e];t++) pre[t+1]=pre[t]+vec[i][e][t];
      uint64_t s=0;
      for(int u=0;u<c[e+1];u++){ vec[i][e+1][u]=pre[lam[u]]; s+=pre[lam[u]]; }
      ent[i][e+1]=s;
    }
    for(int u=0;u<c[e+1];u++) vec[e+1][e+1][u]=1;
    ent[e+1][e+1]=c[e+1];
    dfs(e+1);
  }
}
int main(int argc,char**argv){
  r=argc-2; for(int i=0;i<=r;i++) c[i]=atoi(argv[i+1]);
  int cur[MAXC]; double total=1;
  for(int e=0;e<r;e++){ nproj[e]=0; gen(e,0,0,cur); total*=nproj[e]; }
  tabsize=(uint64_t)(total*2)+1031; tab=calloc(tabsize,sizeof(slot));
  if(!tab){ fprintf(stderr,"alloc failed\n"); return 2; }
  for(int u=0;u<c[0];u++) vec[0][0][u]=1; ent[0][0]=c[0];
  dfs(0);
  printf("DETERMINED: %lld tuples, %lld distinct off-corner data\n",nleaves,ndistinct);
  return 0;
}
