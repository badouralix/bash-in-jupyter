# %%
!kind create cluster


# %%
!kubectx --current


# %%
!kubectl get pods --all-namespaces


# %%
!kubectl run toolbox --image=badouralix/toolbox --command sleep inf


# %%
!kubectl get pods


# %%
!kubectl describe pod toolbox


# %%
!kubectl delete pod toolbox


# %%
!kind delete cluster


# %%
