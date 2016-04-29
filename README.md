# ShowerRefiner

This LArLite repository is designed to contain modules which refine shower quantities after shower reconstruction has been run. This generally involves the comparison of the reconstructed shower profile itself (ie. the cone) with the initial hits and clusters, and resolving any tensions between the two.

## ShowerHitRefiner

This module requires reconstructed shower objects, as well as the clusters and hits associated with this shower. It will loop over all hits in the event, and identify any which are not associated with any shower clusters. It will then compare these unclustered hits with the shower profiles of all showers in the event, and see if it falls inside any cone. A new association from cluster => hit is assigned, as well as a new hit data product, which is identical in content to the original hit data product, but is created regardless to prevent any potential conflicts.

Issues with this module:

- Any "unclustered hits"

