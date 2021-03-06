from ._restartable import Restartable



#===================================================================================================
# Build
#===================================================================================================
class Build(Restartable):
    '''
    :ivar int repository_id:
        Repository ID.

    :ivar str commit_id:
        Commit ID.

    :ivar str number:
        Build number.

    :ivar bool pull_request:
        Whether or not the build comes from a pull request.

    :ivar str pull_request_title:
        PR title if :attr:`pull_request` is ``True``.

    :ivar str pull_request_number:
        PR number if :attr:`pull_request` is ``True``.

    :ivar dict config:
        Build config (secure values and ssh key removed). It comes from ``.travis.yml`` file.

    :ivar str started_at:
        Time the build was started.

    :ivar str finished_at:
        Time the build finished.

    :ivar str duration:
        Build duration. It might not correspond to :attr:`finished_at` - :attr:`started_at` if the
        build was restarted at a later point.

    :ivar list(int) job_ids:
        List of job IDs in the build matrix.
    '''

    __slots__ = [
        'repository_id',
        'commit_id',
        'number',
        'pull_request',
        'pull_request_title',
        'pull_request_number',
        'config',
        'started_at',
        'finished_at',
        'duration',
        'job_ids',
    ]
