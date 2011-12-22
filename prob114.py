import walkera.memoize

def fillCount(m,n):
    @walkera.memoize.memoize
    def impl(m,n):
        cnt = 0
        for i in xrange(m,n+1):
            for j in xrange(i,n+1):
                cnt += 1
                if j-i > m:
                    cnt += impl(m, j-i-1)
        return cnt
    return impl(m,n)+1

if __name__ == "__main__":
    print fillCount(3,50)


