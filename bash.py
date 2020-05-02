# %%
!kind create cluster


# %%
!kubectx --current


# %%
!kubectl get pods --all-namespaces


# %%
!kubectl run toolbox --image=badouralix/toolbox -- sleep inf


# %%
!kubectl get pods


# %%
!kubectl describe pod toolbox


# %%
!time kubectl delete pod toolbox


# %%
!kind delete cluster


# %%
