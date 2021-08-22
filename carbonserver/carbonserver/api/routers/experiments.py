from typing import List
from uuid import UUID

from container import ServerContainer
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette import status

from carbonserver.api.schemas import Experiment, ExperimentCreate
from carbonserver.api.services.experiments_service import ExperimentService

EXPERIMENTS_ROUTER_TAGS = ["Experiments"]

router = APIRouter()


@router.post(
    "/experiment",
    tags=EXPERIMENTS_ROUTER_TAGS,
    status_code=status.HTTP_201_CREATED,
    response_model=UUID,
)
@inject
def add_experiment(
    experiment: ExperimentCreate,
    experiment_service: ExperimentService = Depends(
        Provide[ServerContainer.experiment_service]
    ),
) -> Experiment:
    return experiment_service.add_experiment(experiment)


@router.get(
    "/experiment/{experiment_id}",
    tags=EXPERIMENTS_ROUTER_TAGS,
    status_code=status.HTTP_200_OK,
    response_model=Experiment,
)
@inject
def read_experiment(
    experiment_id: str,
    experiment_service: ExperimentService = Depends(
        Provide[ServerContainer.experiment_service]
    ),
) -> Experiment:
    return experiment_service.get_one_experiment(experiment_id)


@router.get(
    "/experiments/project/{project_id}",
    tags=EXPERIMENTS_ROUTER_TAGS,
    status_code=status.HTTP_200_OK,
    response_model=List[Experiment],
)
@inject
def read_experiment_experiments(
    project_id: str,
    experiment_service: ExperimentService = Depends(
        Provide[ServerContainer.experiment_service]
    ),
) -> List[Experiment]:

    return experiment_service.get_experiments_from_project(project_id)
