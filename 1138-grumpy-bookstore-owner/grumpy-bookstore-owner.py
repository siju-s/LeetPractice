class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        unsatisfied = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfied += customers[i]
                customers[i] = 0 # modifying array to avoid double counting later

        maxUnsatisfied = 0

        for i, customer in enumerate(customers):
            unsatisfied += customer

            if i >= minutes:
                unsatisfied -= customers[i - minutes]

            maxUnsatisfied = max(maxUnsatisfied, unsatisfied)

        return satisfied + maxUnsatisfied     



        