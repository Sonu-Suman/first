from covid import Covid
import matplotlib.pyplot as plt

cov = Covid()

name = input("Enter country name: ")
virusdata = cov.get_status_by_country_name(name)

active= virusdata['active']

recover = virusdata['recovered']

death = virusdata['deaths']

total = virusdata['confirmed']

print(f'Total case of covid: {total}')

print(f'Total active case in {name}: {active}')

print(f'Total death due to corona virus in {name}: {death}')

plt.pie([active, recover, death], labels=[('Active', float('%.2f'%((active * 100)/ total))), ('Recover', float('%.2f'%((recover * 100)/ total))), ('Death', float('%.2f'%((death * 100)/ total)))])

plt.title(name)
plt.legend()

plt.show()
