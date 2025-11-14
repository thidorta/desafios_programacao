Vk, Jk = map(int, input().split())
Vl, Jl = map(int, input().split())
Vh, Dh, Jh = map(int, input().split())

heavy_chain = Vh * Jh * Dh
light_chain_kappa = Vk * Jk
light_chain_lambda = Vl * Jl

total_light_chain = light_chain_kappa + light_chain_lambda

total_final = total_light_chain * heavy_chain

print(total_final)
