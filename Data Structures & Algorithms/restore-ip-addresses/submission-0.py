
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = set()
        if len(s) < 4:
            return results

        def dfs(curr, index, remaining):
            if remaining == 0:
                if curr.count(".") == 3:
                    results.add(curr)
                return

            if index >= len(curr):
                return

            # include a period after index
            if index > 0:
                tmp = curr[:index] + "." + curr[index:]

                # backtrack from index + 2 with remaining -1
                dfs(tmp, index + 2, remaining - 1)

            # remove the dot and go forward
            dfs(curr, index + 1, remaining)

        dfs(s, 0, 3)

        def filter(ip):
            iplist = ip.split(".")
            try:
                for index in range(4):
                    num = int(iplist[index])
                    if num < 0 or num > 255:
                        return
                    if len(iplist[index]) > 1 and iplist[index][0] == "0":
                        return
            except:
                return
            return ".".join(iplist)

        f = []
        for ip in results.copy():
            results.remove(ip)
            ip = filter(ip)
            if ip:
                f.append(ip)

        return f